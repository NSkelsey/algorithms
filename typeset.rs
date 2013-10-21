use std::os; 
use std::io; 
use std::vec; 
use std::num; 

static M: uint = 80;
static BIG: uint = 1024*1024*1024;

fn make_S(words: ~[~str]) -> ~[~[uint]] { 
    let n = words.len();
    let mut S: ~[~[uint]] = ~[];
    let mut i = 0;
    while n > i {
        S.push(vec::from_fn(n, |_| { BIG }));
        i += 1;
    };

    let mut i = 0;
    while i < n {
        let mut j = i;
        while j < n {
            if i == j {
                S[i][j] = M - words[j].len();
            } else {
                let tmp = S[i][j-1] - 1 - words[j].len();
                if tmp > M {
                    break;
                } else {
                    S[i][j] = tmp;
                }
            }
            j += 1;
        };
        i += 1;
    };
    return S
}

fn typeset(words: ~[~str]) -> ~str {
    let n = words.len();
    let mut S = make_S(words.clone());
     
    let mut B: ~[uint] = vec::from_fn(n, |_| { BIG });       
    let mut P: ~[uint] = vec::from_fn(n, |_| { 0 });
    let mut j = 0;

    //println(fmt!("%?", S)); 

    while j < n {
        let mut k = 0; 
        let mut min = BIG;
        let mut soln_tup: uint = 0; // the previous jth word on ith line that composes the solution
        while k < n {   
            let mut val: uint;
            if k == 0 {
                val = S[k][j] << 2; 
            } else {
                val = B[k-1] + (S[k][j] << 2);    
            }
            if min > val { 
                min = val;
                soln_tup = k;
             };
            k += 1;
        }
        P[j] = soln_tup;
        B[j] = min;
        j += 1;
    };
    
    let passage = typeset_passage(words.clone(), P.clone());
    println(fmt!("%?", P)); 
    return passage;
}


fn typeset_passage(words: ~[~str], P: ~[uint]) -> ~str {
    let n = P.len();
    let mut c = n-1;
    let mut passage: ~str = ~"";
    while c > 0 {
        let mut i = c;
        c = P[c];
        while i > c {
            passage =  words[i] + ~" " + passage;
            i -= 1;
        }
        passage = ~"\n" + passage;
        println(fmt!("%?", c)); 
    };
    passage = words[0].clone() + ~" " + passage.slice(1, passage.len());

    return passage;
}



fn main() {
    let args = os::args();
    if args.len() != 2 {
        println(~"Usage: ./typeset filename");
        return 
    }
    let filename = args[1];
    let contents = match io::read_whole_file_str(&os::getcwd().push(filename)) {
        Ok(file_contents) => { file_contents },
        Err(err)          => { println(err); fail!("bad filepath"); }  
    };

    let mut words: ~[~str] =  contents.split_iter(' ').map(|x| x.to_owned()).collect();
    println(typeset(words));
 }
