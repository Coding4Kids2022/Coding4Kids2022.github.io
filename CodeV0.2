//SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract Nft is ERC721 {

    using Counters for Counters.Counter;
    Counters.Counter private CurrentTokenID;
    string public url;

    constructor() ERC721 ("destroyed jungle","jungle"){
        url = "https://raw.githubusercontent.com/Coding4Kids2022/Leo-Leon/main/";
    }

    function mintTo(address recipient)

    public 
    returns (uint256)
    
    {
        CurrentTokenID.increment();
        uint256 newItemId = CurrentTokenID.current();
        _safeMint(recipient, newItemId);
        return newItemId;
    
    }
    
    function tokenURI(uint256 tokenID)public view override returns (string memory){
        return string(abi.encodePacked(url, Strings.toString(tokenID),".json"));
    }

    
}


