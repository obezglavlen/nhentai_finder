import parser from "./parser.js";
import "colors";
import { API } from "nhentai-api";

const args = parser.parse_args();

const api = new API();
api.getBook(args.ID).then((book, err) => {
  if (err) {
    console.log("Could not find doujinsi with id: ".red + args.ID);
    return 1;
  }

  console.log(`Searching for ${book.id}...`.yellow);

  if (args.TITLE) {
    console.log("TITLE: ", `${book.title.pretty}`.green);
  }

  if (args.TAG) {
    console.log("TAG: ", `${book.tags.join(", ")}`.green);
  }
});
