# ashblock

A Shell Blocker, the script for blocking ads on the web.

### Dependencies

- `curl`: for downloading the `hosts` file.
- `cron`: for running the Cron job (if installed).

### Usage

Just double-click the `ashblock` file (after checking if it's executable).

### Cron job

A Cron job that updates the `host` file automagically can be executed daily (at 00:00 UTC time), check [extras/cronjob](https://github.com/feskyde/ashblock/tree/master/extras/cronjob) folder.

### Installation

Run the `INSTALL` script, you can also choose if you want the Cron job to be installed.

### Releases

Lastest: [v2.0](https://github.com/feskyde/ashblock/releases/tag/v2.0) "Betelgeuse".

For old releases go to [RELEASES](https://github.com/feskyde/ashblock/releases) page

### TO-DO

- [x] Add a `cron` job for updating the `hosts` file every week.
- [x] Replace `wget` (now using `curl`).
- [ ] Ports:
  - [ ] Windows.
  - [x] OS X (has a link to this file).
  - [x] BSD and other \*nixes (uses the same file location).

### License

This program is distributed under the [GNU Public License version 2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

Thus, ashblock is **free** (as in freedom and beer) and you can [view](https://github.com/feskyde/ashblock), edit and [fork](https://github.com/feskyde/ashblock/fork) the code if you want.

