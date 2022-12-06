use std::collections::HashSet;

pub fn solve() {
    let bytes = include_str!("../inputs/dec06.txt").as_bytes();

    println!("--- Part One ---");
    println!("{}", find_unique_window_index(bytes, 4) + 4);

    println!("--- Part Two ---");
    println!("{}", find_unique_window_index(bytes, 14) + 14);
}

fn find_unique_window_index(bytes: &[u8], window_size: usize) -> usize {
    bytes
        .windows(window_size)
        .enumerate()
        .find(|index_window_pair| {
            let window = index_window_pair.1;
            window.iter().collect::<HashSet<&u8>>().len() == window_size
        }).unwrap().0
}
