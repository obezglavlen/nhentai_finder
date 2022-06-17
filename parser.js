import { ArgumentParser } from "argparse";
import { readFileSync } from "fs";

const packageJson = JSON.parse(readFileSync("./package.json", "utf8"));

const parser = new ArgumentParser({
  description: "A simple CLI for the NHentai api.",
});

parser.add_argument("ID", {
  help: "The id of the manga to look for.",
});

parser.add_argument("-v", "--version", {
  help: "Show the version of the CLI.",
  action: "version",
  version: `${packageJson.version}`,
});

parser.add_argument("-T", "--title", {
  help: "The title of the manga to look for.",
  action: "store_true",
  dest: "TITLE",
});

parser.add_argument("-t", "-tag", {
  help: "The tag of the manga to look for.",
  action: "store_true",
  dest: "TAG",
});

export default parser;
