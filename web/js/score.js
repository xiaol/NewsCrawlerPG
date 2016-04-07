/**
 * Created by lee on 16-3-23.
 */
$(document).ready(function() {
    $("#score").click(submit);
});

submit = function(){
    $("#content").html("");
    data = {url:$("#url").val()};
    post_url = "/score";
    $.post(
        post_url,
        data,
        parsed_callback,
        "json");
};

parsed_callback = function(data, state){
    content = data["data"];
    inner_html = "";
    for(index in content){
        item = content[index];
        inner_html += "<p>" + item + "</p>"
    }
    $("#content").html(inner_html);
};