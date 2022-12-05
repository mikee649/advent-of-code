use regex::Regex;

pub fn solve() {
    let(starting_stacks_in, rearrangement_in): (Vec<&str>, Vec<&str>)
        = include_str!("../inputs/dec05.txt")
            .lines()
            .filter(|line| line.contains('[') || line.contains("move"))
            .partition(|line| line.contains('['));

    let mut stacks_p1: Vec<Vec<char>> = Vec::new();
    let mut stacks_p2: Vec<Vec<char>> = Vec::new();
    for _ in 0..9 { 
        stacks_p1.push(Vec::new()); 
        stacks_p2.push(Vec::new()); 
    }
    
    starting_stacks_in.iter().for_each(|line| {
        line.chars().enumerate().for_each(|(i, c)| {
            if c.is_alphabetic() {
                stacks_p1[i/4].insert(0, c);
                stacks_p2[i/4].insert(0, c);
            }
        });
    });

    rearrangement_in.iter().for_each(|line| {
        let (amount, from, to) = parse_rearrangement(line);

        apply_move_p1(&mut stacks_p1, amount, from, to);
        apply_move_p2(&mut stacks_p2, amount as usize, from, to);
    });

    println!("--- Part One ---");
    print_stack_tops(stacks_p1);

    println!("--- Part Two ---");
    print_stack_tops(stacks_p2);
}

fn apply_move_p1(stacks: &mut [Vec<char>], amount: u8, from: usize, to: usize) {
    for _ in 0..amount { 
        let val = stacks[from-1].pop().unwrap();
        stacks[to-1].push(val);
    }
}

fn apply_move_p2(stacks: &mut [Vec<char>], amount: usize, from: usize, to: usize) {
    let drain_index = stacks[from-1].len() - amount;
    let drained_vals: Vec<char> = stacks[from-1].drain(drain_index..).collect();
    drained_vals.iter().for_each(|val| stacks[to-1].push(*val));
}

fn parse_rearrangement(line: &str) -> (u8, usize, usize) {
    let reg = Regex::new(
        r"move (?P<amount>[0-9]+) from (?P<from>[0-9]) to (?P<to>[0-9])"
    ).unwrap();

    let captures = reg.captures(line).unwrap();
        
    let amount = &captures["amount"].parse::<u8>().unwrap();
    let from = &captures["from"].parse::<usize>().unwrap();
    let to = &captures["to"].parse::<usize>().unwrap();

    (*amount, *from, *to)
}

fn print_stack_tops(stacks: Vec<Vec<char>>) {
    println!("{}", stacks
        .iter()
        .map(|stack| stack.last().unwrap())
        .collect::<String>()
    );
}
