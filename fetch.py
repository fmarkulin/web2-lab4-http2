const fs = require("fs");

for (let i = 0; i < 100; i++) {
  fetch("https://picsum.photos/350")
    .then((res) => {
      const dest = fs.createWriteStream(`./${i}.jpg`);
      res.body.pipe(dest);
    })
    .catch((err) => console.error(err));
}
