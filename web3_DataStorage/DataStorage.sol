// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract DataStorage {

    uint256  favoriteNumber;
    bool favoriteBool;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
        uint256 test = 4;
    }

    function retrieve() public view returns(unit256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({_favoriteNumber, _name}));
    } 

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({_favoriteNumber, _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}