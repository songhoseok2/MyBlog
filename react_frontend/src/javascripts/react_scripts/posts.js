import React from 'react';
import ReactDOM from 'react-dom';



export class OP_ProfilePic extends React.Component
{
  render()
  {
    return (
      <div>
        <img class="rounded-circle article-img" 
            src="/static/profile_pics/anonymous.png"></img>
      </div>
    );
  }
}


var OP_profile_pic_divs = document.getElementsByClassName("OP_profile_pic_class");
// var OP_annonymousity = OP_profile_pic_div.getAttribute("is_annonymous");


for (var OP_profile_pic_div of OP_profile_pic_divs)
{
    ReactDOM.render(<OP_ProfilePic />, OP_profile_pic_div);
}






