use rand::prelude::*;

// fn _print_type_of<T>(_: &T) {
//     println!("{}", std::any::type_name::<T>());
// }

/// column of index
fn get_col(index: i32) -> i32 {
    index % 9
}

/// all values of the same column of index
fn get_all_in_col(sud: &Vec<i32>, index: i32) -> Vec<i32> {
    let col_n = get_col(index);
    let mut col: Vec<i32> = Vec::new();
    for i in 0..sud.len() {
        if get_col(i.try_into().unwrap()) == col_n {
            col.push(sud[i])
        }
    }
    col.to_vec()
}

/// row of index
fn get_row(index: i32) -> i32 {
    let quot = (index / 9) as f32;
    quot.floor() as i32
}

/// all values of the same row of index
fn get_all_in_row(sud: &Vec<i32>, index: i32) -> Vec<i32> {
    let row_n = get_row(index);
    let mut row: Vec<i32> = Vec::new();
    for i in 0..sud.len() {
        if get_row(i.try_into().unwrap()) == row_n {
            row.push(sud[i])
        }
    }
    row.to_vec()
}

/// square of index
fn get_square(index: i32) -> i32 {
    let row = get_row(index);
    let col = get_col(index);
    let row_quot = (row / 3) as f32;
    let col_quot = (col / 3) as f32;
    ((3.0 * row_quot.floor()) + col_quot.floor()) as i32
    
}

/// all values of the same square of index
fn get_all_in_square(sud: &Vec<i32>, index: i32) -> Vec<i32> {
    let square_n = get_square(index);
    let mut square: Vec<i32> = Vec::new();
    for i in 0..sud.len() {
        if get_square(i.try_into().unwrap()) == square_n {
            square.push(sud[i])
        }
    }
    square.to_vec()
}

/// check collision: f
fn does_collide(sud: &Vec<i32>, index: i32, val: i32) -> bool {
    let col = get_all_in_col(sud, index);
    let square = get_all_in_square(sud, index);
    let row = get_all_in_row(sud, index);

    let col_collides = col.contains(&val);
    let row_collides = row.contains(&val);
    let square_collides = square.contains(&val);
    
    col_collides || row_collides || square_collides
}

fn generate_sudoku() -> (Vec<i32>, usize) {
    let mut finished_sud = vec![0; 81];
    let mut fail_count: usize = 0;
    while fail_count < 1000 {
        let mut sud = vec![0; 81];
        let mut fail = false;
        for i in 0..sud.len() {
            let mut choices = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];
            while choices.len() > 0 {
                let random_in_range = rand::thread_rng().gen_range(0..choices.len());
                let choice = choices[random_in_range];

                if does_collide(&sud, i.try_into().unwrap(), choice) {
                    choices.retain(|&x| x != choice);
                }
                else {
                    sud[i] = choice;
                    break
                }
            }
            if choices.len() == 0 {
                fail = true;
            }

            if fail { break }
        }
        if fail {
            fail_count += 1;
        }
        else {
            finished_sud = sud;
            break
        }
    }

    (finished_sud.to_vec(), fail_count)
}

fn print_sudoku(sud: &Vec<i32>) {
    for i in 0..sud.len() {
        let val = sud[i];
        if i % 9 == 8 {
            print!("{val}\n");
        }
        else { print!("{val} "); }
    }
    println!();
}

fn checker(sud: &Vec<i32>) -> bool{
    let mut fail = false;
    for i in 0..sud.len() {
        if does_collide(sud, i.try_into().unwrap(), sud[i]) {
            fail = true;
        }
    }
    fail
}

fn main() {
    let sudoku = generate_sudoku();
    let finished_sudoku = sudoku.0;
    let fail_count = sudoku.1;
    print_sudoku(&finished_sudoku);
    println!("fail count: {fail_count}");
    let checked = checker(&finished_sudoku);
    println!("is valid sudoku: {checked}");
}
