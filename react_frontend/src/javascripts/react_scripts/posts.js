import React from 'react';
import ReactDOM from 'react-dom';


export class OP_ProfilePic extends React.Component
{
  render()
  {
    return <img class="rounded-circle article-img" src="/static/profile_pics/anonymous.png"></img>;
  }
}


var OP_profile_pic_divs = document.getElementsByClassName("OP_profile_pic_class");
for (var OP_profile_pic_div of OP_profile_pic_divs)
{
    ReactDOM.render(<OP_ProfilePic />, OP_profile_pic_div);
}






