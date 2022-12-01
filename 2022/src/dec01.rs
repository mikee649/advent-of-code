use std::cmp;

pub fn solve() {
    let mut max_arr = [0, 0, 0];
    let mut sum = 0;
    
    for line in include_str!("../inputs/dec01.txt").lines() {
        if line.is_empty() {
            let (min_index, min_val) = max_arr.iter().enumerate().min_by(|(_, a), (_, b)| a.cmp(b)).unwrap();
            max_arr[min_index] = cmp::max(*min_val, sum);

            sum = 0;
        } else {
            sum += line.parse::<u32>().unwrap();
        }
    }

    println!("--- Part One ---");
    println!("{}", max_arr.iter().max().unwrap());

    println!("--- Part Two ---");
    println!("{}", max_arr.iter().sum::<u32>());
}
