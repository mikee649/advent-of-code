pub fn solve() {
    let range_pair_iter = include_str!("../inputs/dec04.txt")
        .lines()
        .map(|line| { 
            let comma_split: Vec<&str> = line.split(',').collect();
            (Range::from_str(comma_split[0]), Range::from_str(comma_split[1])) 
        });

    println!("--- Part One ---");
    println!("{}", range_pair_iter.clone()
        .filter(|ranges| ranges.0.contains(&ranges.1) || ranges.1.contains(&ranges.0))
        .count()
    );

    println!("--- Part Two ---");
    println!("{}", range_pair_iter
        .filter(|ranges| ranges.0.overlaps(&ranges.1))
        .count()
    );
}

struct Range {
    start: u8,
    end: u8
}

impl Range {
    fn from_str(string: &str) -> Range {
        let split = string.split('-').collect::<Vec<&str>>();
        Range { start: split[0].parse().unwrap(), end: split[1].parse().unwrap() }
    }

    fn contains(&self, other: &Range) -> bool {
        self.start <= other.start && self.end >= other.end
    }

    fn overlaps(&self, other: &Range) -> bool {
        self.start <= other.start && self.end >= other.start ||
            other.start <= self.start && other.end >= self.start
    }
}
