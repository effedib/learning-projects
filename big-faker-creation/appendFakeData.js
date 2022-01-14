const fs = require('fs-extra');
const { getFakeOrder } = require("./getFakeOrders");
const file = 'fake_data_append.csv';
const outputFile = `${__dirname}\\csv2upload\\${file}`


function appendFake () {

    // I use 2 for loops to generate and write data in blocks
    for (let i=0; i<=250; i++) {
        for (let j=0; j<=10000; j++) {

          // getFakeOrder creates the fake data, appendFileSync writes the data in the csv, if it doesn't exists, it create the file.
          fs.appendFileSync(outputFile, getFakeOrder(), (err) => {
            // if an error occurs, diplay the error
            if (err) {console.log(err)};
            return;
          });
      
        }
        // display the status every 100k rows
        if ((i%10)===0) {console.log(`Updated block ${i}, file ${file}`)};
      }
      
      console.log(`Test Terminated`);
}


module.exports = {
    appendFake
  }