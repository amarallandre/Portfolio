
function closePopup(popupId) {
  document.getElementById(popupId).style.display = "none";
}
function openPopup(popupId) {
  document.getElementById(popupId).style.display = "block";
  document.querySelector(".popup-image").src = image.src;
}
