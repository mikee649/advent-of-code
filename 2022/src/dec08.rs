use std::cmp;
use std::collections::HashSet;

pub fn solve() {
    let grid: Vec<Vec<u16>> = include_str!("../inputs/dec08.txt")
        .lines()
        .map(|line| line.chars().map(|c| c as u16 - 48).collect::<Vec<u16>>() )
        .collect();

    println!("--- Part One ---");
    println!("{}", trees_seen_from_outside_grid(&grid));

    println!("--- Part Two ---");
    let mut largest_viewing_angle = 0;
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            largest_viewing_angle = cmp::max(largest_viewing_angle, viewing_angle(grid.to_vec(), i, j));
        }
    }
    println!("{}", largest_viewing_angle);
}

fn trees_seen_from_outside_grid(grid: &Vec<Vec<u16>>) -> usize {
    let mut seen_trees: HashSet<(usize, usize)> = HashSet::new();
    grid
        .iter()
        .enumerate()
        .for_each(|(index, row)| {
            check_seen_trees(row.to_vec()).iter().for_each(|tree_index| {
                seen_trees.insert((index, *tree_index));
            });
            check_seen_trees(reversed(row.to_owned())).iter().for_each(|tree_index| {
                seen_trees.insert((index, grid[0].len() - 1 - *tree_index));
            });
        });

    for i in 0..grid[0].len() {
        let column = grid.iter().map(|row| row[i]).collect::<Vec<u16>>();
        let reversed = reversed(column.to_owned());

        check_seen_trees(column).iter().for_each(|tree_index| {
            seen_trees.insert((*tree_index, i));
        });
        check_seen_trees(reversed).iter().for_each(|tree_index| {
            seen_trees.insert((grid.len() - 1 - *tree_index, i));
        });
    } 

    seen_trees.len()
}

fn check_seen_trees(trees: Vec<u16>) -> Vec<usize> {
    let mut seen_trees: Vec<usize> = vec![0];
    let mut tallest_seen = trees[0];

    for (i, tree) in trees.iter().enumerate().skip(1) {
        if *tree > tallest_seen {
            seen_trees.push(i);
            tallest_seen = *tree;
        }
    }

    seen_trees
}

fn viewing_angle(grid: Vec<Vec<u16>>, row_index: usize, col_index: usize) -> u32 {
    let row = &grid[row_index];
    let col = grid.iter().map(|row| row[col_index]).collect::<Vec<u16>>();

    let view_east = iterations_until_limit(&row[col_index+1..row.len()].to_vec(), row[col_index]);
    let view_west = iterations_until_limit(&reversed(row[0..col_index].to_vec()), row[col_index]);
    let view_south = iterations_until_limit(&col[row_index+1..col.len()].to_vec(), col[row_index]);
    let view_north = iterations_until_limit(&reversed(col[0..row_index].to_vec()), col[row_index]);

    view_east * view_west * view_south * view_north
}

fn iterations_until_limit(vec: &Vec<u16>, limit: u16) -> u32 {
    let mut iterations = 0;
    for i in vec {
        iterations += 1;
        if *i >= limit {
            break;
        }
    }
    iterations
}

fn reversed(vec: Vec<u16>) -> Vec<u16> {
    vec.iter().rev().map(|val| val.to_owned()).collect()
}
