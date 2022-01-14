const fs = require('fs-extra');
const { getFakeOrder } = require("./getFakeOrders");
const streamFile = 'fake_data_stream.csv';
const outputFile = `${__dirname}\\csv2upload\\${streamFile}`;



function writeFakeDataStreams () {
  // create the stream object
  const myWriteStream = fs.createWriteStream(outputFile);
  // I use 2 for loops to generate and write data in chunks
  for (let i=0; i<=70; i++) {
      for (let j=0; j<=100000; j++) {
        myWriteStream.write(getFakeOrder());
      }
    }
}

module.exports = {
    writeFakeDataStreams
}