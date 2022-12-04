use std::collections::HashSet;

pub fn solve() {
    println!("--- Part One ---");
    println!("{}", include_str!("../inputs/dec03.txt")
        .lines()
        .fold(0, |acc, line| {
            let halves = line.split_at(line.len() / 2);
            let first_half_char_map: HashSet<char> = halves.0.chars().collect();
            let letter = halves.1.chars().find(|c| first_half_char_map.contains(c)).unwrap();

            acc + points_for_letter(letter)
        })
    );

    println!("--- Part Two ---");
    println!("{}", include_str!("../inputs/dec03.txt")
        .lines()
        .map(|line| { line.chars().collect::<HashSet<char>>() })
        .collect::<Vec<HashSet<char>>>()
        .chunks(3)
        .fold(0, |acc, chunk| {
            let letter = chunk[2].iter().copied().find(|c| {
                chunk[0].contains(c) && chunk[1].contains(c)
            }).unwrap();

            acc + points_for_letter(letter)
        })
    );
}

fn points_for_letter(letter: char) -> u16 {
    (if letter >= 'a' {letter as u8 - 96} else {letter as u8 - 64 + 26}) as u16
}
