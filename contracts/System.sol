//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
contract System{
    bytes32 private constant ADMIN = keccak256(abi.encodePacked("ADMIN"));
    bytes32 private constant SUDO = keccak256(abi.encodePacked("SUDO"));
    bytes32 private constant USER = keccak256(abi.encodePacked("USER"));
    string private verification;
    mapping(bytes32 => mapping(address => bool)) access;
    // 1st => Admin || 2nd => Sudo || 3rd => user
    modifier onlyUser(bool admin,bool sudo,bool user){
        if(access[ADMIN][msg.sender]){
            require(admin,"Access Denied!");
            _;
        }
        else if(access[SUDO][msg.sender]){
            require(sudo,"Access Denied");
            _;
        }
        else{
            require(user,"Access Denied");
            _;
        }
    }
    constructor(string memory _verification){
        verification = _verification;
        access[ADMIN][msg.sender] = true;
    }
    function getKey() public onlyUser(true,true,false) view returns(string memory){
        return verification;
    }
    function _addUser(address _user) internal{
        access[USER][_user] = true;
    }
    function addUser(address _user) external onlyUser(true,false,false){
        _addUser(_user);
    }
    function _removeUser(address _user) internal {
        access[USER][_user] = false;
        access[SUDO][_user] = false;
    }
    function removeUser(address _user) external onlyUser(true,false,false){
        _removeUser(_user);
    }
    function _grantSudo(address _user) internal{
        access[SUDO][_user] = true;
        access[USER][_user] = false;
    }
    function grantSudo(address _user) external onlyUser(true,false,false){
        _grantSudo(_user);
    }
}