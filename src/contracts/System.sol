//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
contract System{
    event Fetch(address indexed user);
    mapping(bytes32 => mapping(address => bool)) roles;
    bytes32 private constant ADMIN = keccak256(abi.encodePacked("ADMIN"));
    bytes32 private constant USER = keccak256(abi.encodePacked("USER"));
    // modifier onlyRole(bytes32 role){
    //     require(roles[role][msg.sender],"Access Denied!");
    //     _;
    // }
    // modifier recordExist(address _user){
    //     require(roles[USER][_user],"Record Doesnt Exist");
    //     _;
    // }
    // modifier recordNotExist(address _user){
    //     require(roles[USER][_user] == false,"Record Exist");
    //     _;
    // }
    constructor(){
        roles[ADMIN][msg.sender] = true;
    }
    function _addRecord(address _newUser) internal {
        roles[USER][_newUser] = true;
    }
    function _removeRecord(address _user) internal {
        roles[USER][_user] = false;
    }
    // function removeRecord(address _user) external onlyRole(ADMIN) recordExist(_user){
    //     _removeRecord(_user);
    // }
    // function addRecord(address _newUser) external onlyRole(ADMIN) recordNotExist(_newUser){
    //     _addRecord(_newUser);
    // }
    // function fetch() external onlyRole(USER){
    //     emit Fetch(msg.sender);
    // }
    function removeRecord(address _user) external{
        if(roles[ADMIN][msg.sender] && roles[USER][_user]){
            _removeRecord(_user);
        }
    }
    function addRecord(address _newUser) external{
        if(roles[ADMIN][msg.sender] && !roles[USER][_newUser]){
            _addRecord(_newUser);
        }
    }
    function fetch() external{
        emit Fetch(msg.sender);
    }
}