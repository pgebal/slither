pragma solidity ^0.8.19;
contract Owner{

    address owner;

    modifier onlyOwner(){
        require(msg.sender == owner);
        _;
    }

}

contract MyContract is Owner{

    mapping(address => uint) balances;

    constructor() public{
        owner = msg.sender;
    }

    function mint(uint value) onlyOwner public{
        balances[msg.sender] += value;
    }    

}
