use std::collections::HashSet;

pub fn solve() {

    println!("--- Part One ---");
    println!("{}", simulate_tail(2));

    println!("--- Part Two ---");
    println!("{}", simulate_tail(10));
}

fn simulate_tail(num_knots: usize) -> usize {
    let mut knots = vec![(0, 0); num_knots as usize];

    let mut tail_positions: HashSet<(i32, i32)> = HashSet::new();

    for line in include_str!("../inputs/dec09.txt").lines() {
        let mut split = line.split(' ');
        let dir = &split.next().unwrap().chars().next().unwrap(); 
        let num_steps = split.next().unwrap().parse::<u8>().unwrap();

        for _ in 0..num_steps {
            // Move the head
            match dir {
                'R' => knots[0] = (knots[0].0 + 1, knots[0].1),
                'L' => knots[0] = (knots[0].0 - 1, knots[0].1),
                'D' => knots[0] = (knots[0].0, knots[0].1 + 1),
                'U' => knots[0] = (knots[0].0, knots[0].1 - 1),
                _ => panic!("Invalid direction"),
            }

            // Move the subsequent knots
            for i in 1..knots.len() {
                if should_move(knots[i-1], knots[i]) {
                    match knots[i-1].0.cmp(&knots[i].0) {
                        std::cmp::Ordering::Greater => knots[i] = (knots[i].0 + 1, knots[i].1),
                        std::cmp::Ordering::Less => knots[i] = (knots[i].0 - 1, knots[i].1),
                        _ => (),
                    }

                    match knots[i-1].1.cmp(&knots[i].1) {
                        std::cmp::Ordering::Greater => knots[i] = (knots[i].0, knots[i].1 + 1),
                        std::cmp::Ordering::Less => knots[i] = (knots[i].0, knots[i].1 - 1),
                        _ => (),
                    }
                }
            }
            tail_positions.insert(*knots.last().unwrap());
        }
    }

    tail_positions.len()
}

fn should_move(leader: (i32, i32), follower: (i32, i32)) -> bool {
    leader.0 - follower.0 > 1 
        || leader.0 - follower.0 < -1 
        || leader.1 - follower.1 > 1 
        || leader.1 - follower.1 < -1
}
