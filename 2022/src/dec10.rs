pub fn solve() {
    let mut step_count = 0;
    let mut x = 1;
    let mut tmp = 0;
    
    let mut part1_sum = 0;
    let mut part2_output: Vec<char> = Vec::new();

    let mut line_iter = include_str!("../inputs/dec10.txt").lines().peekable();
    while line_iter.peek().is_some() || tmp != 0 {
        step_count += 1;

        if (step_count-20) % 40 == 0 {
            part1_sum += x * step_count;
        }

        let position = (step_count - 1) % 40;
        if position % 40 == 0 {
            part2_output.push('\n') 
        }
        part2_output.push(if (position - x as i32).abs() <= 1 { '█' } else { ' ' }); 

        if tmp != 0 {
            x += tmp;
            tmp = 0;
            continue;
        } 
        
        let line = line_iter.next().unwrap();
        if line == "noop" {
            continue;
        }

        tmp = line.split(' ').nth(1).unwrap().parse::<i32>().unwrap();
    }

    println!("--- Part One ---");
    println!("{}", part1_sum);

    println!("--- Part Two ---");
    println!("{}", part2_output.iter().skip(1).collect::<String>())
}
