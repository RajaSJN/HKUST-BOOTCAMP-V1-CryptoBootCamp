//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
contract Key{
    uint hashDigit = 255;
    uint public hashModulus = 2 ** hashDigit;
    string verification = "dummy";
    function rand() public view returns(uint){
        return uint(keccak256(abi.encodePacked(block.timestamp,block.difficulty,msg.sender)))%hashDigit;
    }
    function hash(string memory _str) public view returns(bytes32){
        bytes32 qrEncoded = sha256(abi.encodePacked(_str));
        bytes32 verificationEncoded = sha256(abi.encodePacked(verification));
        bytes memory combineEncoded = abi.encodePacked(qrEncoded,verificationEncoded);
        uint256 counter = 0;
        bytes32 nonceInt = bytes32(counter);
        bytes memory finalCombine = abi.encodePacked(combineEncoded,nonceInt);
        bytes32 result = sha256(abi.encodePacked(nonceInt,finalCombine));
        bool oneZero = false;
        bytes32 list = "";
        while(oneZero == false){
            nonceInt = bytes32(++counter);
            finalCombine = abi.encodePacked(combineEncoded,nonceInt);
            result = sha256(abi.encodePacked(nonceInt,finalCombine));
            oneZero = true;
            list = bytes32(abi.encodePacked(result,list,"\n"));
            for(uint256 i=0;i<32;++i){
                if(i == 0 && (result[i] >> 4) != 0x00){
                    oneZero = false;
                    break;
                }
                else if(i == 0 && (result[i] << 4) == 0x00){
                    oneZero = false;
                    break;
                }
                if(i != 0 && (result[i] >> 4) == 0x00){
                    oneZero = false;
                    break;
                }
                else if(i != 0 && (result[i] << 4) == 0x00){
                    oneZero = false;
                    break;
                }
            }
        }
        return result;
    }
}