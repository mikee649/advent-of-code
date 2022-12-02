use std::collections::HashMap;

pub fn solve() {
    #[allow(clippy::identity_op)]
    let points_part1 = HashMap::from([
        ("A X", 1 + 3),
        ("B X", 1 + 0),
        ("C X", 1 + 6),
        ("A Y", 2 + 6),
        ("B Y", 2 + 3),
        ("C Y", 2 + 0),
        ("A Z", 3 + 0),
        ("B Z", 3 + 6),
        ("C Z", 3 + 3),
    ]); 

    #[allow(clippy::identity_op)]
    let points_part2 = HashMap::from([
        ("A X", 0 + 3),
        ("B X", 0 + 1),
        ("C X", 0 + 2),
        ("A Y", 3 + 1),
        ("B Y", 3 + 2),
        ("C Y", 3 + 3),
        ("A Z", 6 + 2),
        ("B Z", 6 + 3),
        ("C Z", 6 + 1),
    ]); 

    let answers = include_str!("../inputs/dec02.txt")
        .lines()
        .fold([0, 0], |acc, line| {[
            acc[0] + points_part1.get(line).unwrap(),
            acc[1] + points_part2.get(line).unwrap(),
        ]});

    println!("--- Part One ---");
    println!("{}", answers[0]);

    println!("--- Part Two ---");
    println!("{}", answers[1]);
}
