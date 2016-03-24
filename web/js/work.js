/**
 * Created by lee on 16-3-23.
 */
$(document).ready(function() {
    $("#parse").click(submit);
});

submit = function(){
    $("#news").html("");
    data = {key:$("#keys").val(), url:$("#url").val()};
    post_url = "/";
    $.post(
        post_url,
        data,
        parsed_callback,
        "json");
};

parsed_callback = function(data, state){
    title = data["title"];
    content = data["content"];
    inner_html = "";
    inner_html = inner_html + "<h3 class='text-center'>" + title + "</h3>";
    for(index in content){
        item = content[index];
        if(item["text"]){
            inner_html += "<p>" + item["text"] + "</p>";
        } else if(item["img"]){
            inner_html += "<p class='bg-success'>" + item["img"] + "</p>";
        }
    }
    $("#news").html(inner_html);
};




