
$(function(){
if ($("#personne_photo").length > 0 || $("#lieu_photo").length > 0){
var fileElem=$("#personne_photo").length > 0 ? personne_photo : lieu_photo;
fileElem.addEventListener("change", handleFiles, false);

function handleFiles() {
  if (!this.files.length) {
    fileList.innerHTML = "<p>Aucun fichier sélectionné !</p>";
  } else {
    fileList.innerHTML = "";
    const list = document.createElement("ul");
    fileList.appendChild(list);
    for (let i = 0; i < this.files.length; i++) {
      const li = document.createElement("li");
      list.appendChild(li);

      const img = document.createElement("img");
      img.src = URL.createObjectURL(this.files[i]);
      img.height = 60;
      img.onload = () => {
        URL.revokeObjectURL(img.src);
      };
      li.appendChild(img);
      const info = document.createElement("span");
      info.innerHTML = `${this.files[i].name} : ${this.files[i].size} octets`;
      li.appendChild(info);
    }
  }
}
}


});
