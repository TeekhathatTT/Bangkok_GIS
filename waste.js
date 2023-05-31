function load(layer){

    layer.on('popupopen', function (e) {
        var popup = e.popup;
        var popupData = popup.getElement().getElementsByClassName('popup-data2554')[0];

        var toggleArrow = popupData.getElementsByClassName('toggle-arrow')[0];
        toggleArrow.addEventListener('click', function () {
          this.classList.toggle('open');
      
      
        });
      });

      layer.on('popupopen', function (e) {
        var popup = e.popup;
        var popupData = popup.getElement().getElementsByClassName('popup-data2555')[0];

        var toggleArrow = popupData.getElementsByClassName('toggle-arrow')[0];
        toggleArrow.addEventListener('click', function () {
          this.classList.toggle('open');
      
      
        });
      });

      layer.on('popupopen', function (e) {
        var popup = e.popup;
        var popupData = popup.getElement().getElementsByClassName('popup-data2556')[0];

        var toggleArrow = popupData.getElementsByClassName('toggle-arrow')[0];
        toggleArrow.addEventListener('click', function () {
          this.classList.toggle('open');
           });
        });
    
}