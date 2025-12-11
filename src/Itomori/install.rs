//  SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com

//  SPDX-License-Identifier: 	GPL-3.0-or-later

use std::process::Command;

fn main() {
    let status = Command::new("uv")
        .arg("tool")
        .arg("install")
        .arg("git+https://github.com/TheAhumMaitra/Itomori.git")
        .status()
        .expect("Failed to execute command");

    println!("Command exited with: {}", status);
}
