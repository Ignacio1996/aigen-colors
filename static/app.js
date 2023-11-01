const form = document.getElementById("form"); // Removed the '#' symbol
form.addEventListener("submit", function (e) {
  e.preventDefault();
  console.log("index.html 18 | form", form.elements[0].value);
  const query = form.elements[0].value;
  fetch("/palette", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({ query: query }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("index.html 29 | data", data);
      const colors = data.colors;
      const container = document.querySelector(".container");
      for (const color of colors) {
        const div = document.createElement("div");
        div.classList.add(color);
        div.style.backgroundColor = color;
        div.style.flex = 1;
        div.style.height = "100vh";

        div.addEventListener("click", () => {
          navigator.clipboard.writeText(color);
        });

        const span = document.createElement("span");
        span.innerText = color;
        span.style.margin = "0 auto";
        span.style.width = "100%";
        div.appendChild(span);
        container.appendChild(div);
      }
    })
    .catch((error) => {
      console.log("index.html 30 | ", "error with request", error);
    });
});
