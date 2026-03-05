// Move title → data-title on <abbr> to suppress native browser tooltip
// while keeping the value accessible to our CSS ::after tooltip.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("abbr[title]").forEach(function (el) {
    el.setAttribute("data-title", el.getAttribute("title"));
    el.removeAttribute("title");
  });
});
