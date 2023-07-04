pragma solidity ^0.8.19;

contract Test {
   
  function foo() public returns (address) {
    address from = msg.sender;
    return(from);
  }
}
