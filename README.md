# ashblock/apyblock

A Shell Blocker/APyBlock, the script for blocking annoying ADs on the web.

### Dependencies

- `curl`: for downloading the `hosts` file.
- `cron`: for running the Cron job (if installed).
- For ApyBlock: `python3.2` or greater.

### Usage

Just execute the `ashblock` script in a terminal.

You can change the hosts file source by executing `ashblock source [URL]`!

Optionally, you can try the new Python 3 port, `apyblock`!

### Cron job

A Cron job that updates the `host` file automagically can be executed daily (at 12:00AM UTC time).

### Installation

Run the `INSTALL` script, you can also choose if you want the Cron job to be installed.

### Releases

- Upcoming: v3.0 "Cygnus" (master).

- Current: [v2.1](https://github.com/feskyde/ashblock/releases/tag/v2.1) "Betelgeuse".

- For old releases go to [RELEASES](https://github.com/feskyde/ashblock/releases) page.

### TO-DO

- [x] Add a `cron` job for updating the `hosts` file every day.
- [x] Replace `wget` (now using `curl`).
- [x] Start Python 3 port (`apyblock`).
- [ ] Finish Python 3 port.
    - [ ] Replace shell commands with Python functions.
    - [x] Add a cron job.
- [ ] OS support (listed as OS name :point_right: `File to replace`):
    - [x] GNU/Linux and BSD :point_right: `/etc/hosts`.
    - [x] OS X :point_right: `/private/etc/hosts`.
    - [ ] Windows (low priority) :point_right: `%SystemRoot%\System32\drivers\etc\hosts`.
    - [ ] ReactOS (low priority) :point_right: `reactos\system32\drivers\etc\hosts`.

### License

A Shell Blocker is distributed under the [GNU Public License version 2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

Thus, A Shell Blocker is **free** (as in freedom and beer) and you can [view](https://github.com/feskyde/ashblock), edit and [fork](https://github.com/feskyde/ashblock/fork) the code if you want.

