$(window).on("load", function () {
  if ($("#dailywork_create").length) {
    $.each($("div.weekday"), function (i, val) {
      if ($(val).text() === "土") {
        // 土曜日の場合
        $(val).addClass("saturday");
        $(".saturday").css({
          color: "#0000ff",
        });
      } else if ($(val).text() === "日" || $(val).text() === "祝") {
        // 日曜日の場合
        $(val).addClass("sunday");
        $(".sunday").css({
          color: "#ff0000",
        });
      } else {
        // 平日の場合
        $(val).addClass("workday");
      }
    });
    $("div.contents-menu").css("height", "260%");
    $("div.contents-submenu").css("height", "260%");
  }
});

function onSubmit() {
  var yyyymm = $("#yyyymm").val();
  $("#hidden-yyyymm").val(yyyymm);
}