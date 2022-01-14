# Crack the Caesar Cipher

An exercise to crack the Caesar Cipher. <br />
You can find three test cases inside the `/cases` directory.
The algorithm finds the shift factor for each of them, then returns the decoded text.

Method used: word frequency to analyze the content and determine the shift factor: [https://en.wikipedia.org/wiki/Letter_frequency](https://en.wikipedia.org/wiki/Letter_frequency).

## How to run

```bash
tsc index.ts
node index.js
```