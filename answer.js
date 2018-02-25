const hashLookup = require('./tables/hashLookup');
const hashMap    = require('./tables/hashMap');
const forMatlab  = true;

const isValid = (nums, added) => {
  let a, b, c;

  if (nums.length < 3 ) { return true;}
  nums += added;
  for (let item of nums) {
    switch (item) {
      case 'a':
        a = true;
        break;

      case 'b':
        b = true;
        break;

      case 'c':
        c = true;
        break;

      default:
        console.log('Error');
        break;
    }
  }

  return (a && b && c) ? true : false;
}

function *tStates() {
  yield 'a';
  yield 'b';
  yield 'c';
}

const regulateSpace = item => {
  if (item.length === 0)
    return `nul`;

  if (item.length === 1)
    return `${item}  `;

  if (item.length == 2)
    return `${item} `;

  return item;
}

const createAndPrint = () => {
  var array = new Array(37);
  for (var i = 0; i < 37; i++) {
    array[i] = new Array(37).fill(0);
  }
  let state, iter, accum, storedState;

  for (let i = 1; i <= 37; i++) {
    storedState = hashMap[i]
    for (item of tStates()) {
      if (isValid(storedState, item)) {
        state = storedState + item;
        state = state.length === 4 ? state.slice(1,4) : state;
        array[i-1][hashLookup[state] - 1] += 1;
      }
    }
  }

  if (!forMatlab) {
    iter = 0
    for (item in hashLookup) {
      console.log(`${regulateSpace(item)} : ${JSON.stringify(array[iter++])}`);
    }
  } else {
    for (let i = 0; i < array.length; i++) {
      console.log(JSON.stringify(array[i]))
    }
  }
}

createAndPrint();
