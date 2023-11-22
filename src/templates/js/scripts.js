<script>

     // Fonction pour sauvegarder les sélections dans le stockage local
    function sauvegarderSelections() {
      const selects = document.querySelectorAll('select');
      selects.forEach(select => {
        const id = select.id;
        const selectedIndex = select.selectedIndex;
        localStorage.setItem(id, selectedIndex);
      });
    }

    // Fonction pour charger les sélections depuis le stockage local
    function chargerSelections() {
      const selects = document.querySelectorAll('select');
      selects.forEach(select => {
        const id = select.id;
        const selectedIndex = localStorage.getItem(id);
        if (selectedIndex !== null) {
          select.selectedIndex = selectedIndex;
        }
      });
    }

    function reinitialiserSelections() {
  const selects = document.querySelectorAll('select');
  selects.forEach(select => {
    select.selectedIndex = 0; // Réinitialiser la sélection à l'option par défaut
    localStorage.removeItem(select.id); // Supprimer l'élément correspondant du stockage local
  });

  updateRecapitulatif(); // Mettre à jour le récapitulatif après la réinitialisation
}


    function updateRecapitulatif() {
      const processeurSelect = document.getElementById('processeur');
      const carteGraphiqueSelect = document.getElementById('carte_graphique');
      const carteMereSelect = document.getElementById('carte_mere');
      const memoireViveSelect = document.getElementById('memoire_vive');
      const ssdSelect = document.getElementById('ssd');
      const disqueDurSelect = document.getElementById('disque_dur');
      const alimentationSelect = document.getElementById('alimentation');
      const boitierSelect = document.getElementById('boitier');
      const refroidissementSelect = document.getElementById('refroidissement');

      const composantsSelectionnes = document.getElementById('composants-selectionnes');
      const prixTotalElement = document.getElementById('prix-total');
      const thumbnailSize = 'w-1/3';

      let prixTotal = 0;
      composantsSelectionnes.innerHTML = '';

      let selectedOption = processeurSelect.selectedIndex;
      if (selectedOption !== 0) {
        const prixProcesseur = parseFloat(processeurSelect.options[selectedOption].getAttribute('data-prix').replace(',', '.'));
        const processeurThumbnail = processeurSelect.options[selectedOption].getAttribute('data-thumbnail');
        composantsSelectionnes.innerHTML += '<li class="mb-4">' + processeurSelect.options[selectedOption].text + '</li>';
        composantsSelectionnes.innerHTML += '<li class="mb-4"><img src="' + processeurThumbnail + '" alt="Thumbnail" class="' + thumbnailSize + '"></li>';
        prixTotal += prixProcesseur;
      }

      selectedOption = carteGraphiqueSelect.selectedIndex;
      if (selectedOption !== 0) {
        const prixCarteGraphique = parseFloat(carteGraphiqueSelect.options[selectedOption].getAttribute('data-prix').replace(',', '.'));
        const carteGraphiqueThumbnail = carteGraphiqueSelect.options[selectedOption].getAttribute('data-thumbnail');
        composantsSelectionnes.innerHTML += '<li class="mb-4">' + carteGraphiqueSelect.options[selectedOption].text + '</li>';
        composantsSelectionnes.innerHTML += '<li class="mb-4"><img src="' + carteGraphiqueThumbnail + '" alt="Thumbnail" class="' + thumbnailSize + '"></li>';
        prixTotal += prixCarteGraphique;
      }

      selectedOption = carteMereSelect.selectedIndex;
      if (selectedOption !== 0) {
        const prixCarteMere = parseFloat(carteMereSelect.options[selectedOption].getAttribute('data-prix').replace(',', '.'));
        const carteMereThumbnail = carteMereSelect.options[selectedOption].getAttribute('data-thumbnail');
        composantsSelectionnes.innerHTML += '<li class="mb-4">' + carteMereSelect.options[selectedOption].text + '</li>';
        composantsSelectionnes.innerHTML += '<li class="mb-4"><img src="' + carteMereThumbnail + '" alt="Thumbnail" class="' + thumbnailSize + '"></li>';
        prixTotal += prixCarteMere;
      }

      selectedOption = memoireViveSelect.selectedIndex;
      if (selectedOption !== 0) {
        const prixMemoireVive = parseFloat(memoireViveSelect.options[selectedOption].getAttribute('data-prix').replace(',', '.'));
        const memoireViveThumbnail = memoireViveSelect.options[selectedOption].getAttribute('data-thumbnail');
        composantsSelectionnes.innerHTML += '<li class="mb-4">' + memoireViveSelect.options[selectedOption].text + '</li>';
        composantsSelectionnes.innerHTML += '<li class="mb-4"><img src="' + memoireViveThumbnail + '" alt="Thumbnail" class="' + thumbnailSize + '"></li>';
        prixTotal += prixMemoireVive;
      }

      selectedOption = ssdSelect.selectedIndex;
      if (selectedOption !== 0) {
        const prixSSD = parseFloat(ssdSelect.options[selectedOption].getAttribute('data-prix').replace(',', '.'));
        const ssdThumbnail = ssdSelect.options[selectedOption].getAttribute('data-thumbnail');
        composantsSelectionnes.innerHTML += '<li class="mb-4">' + ssdSelect.options[selectedOption].text + '</li>';
        composantsSelectionnes.innerHTML += '<li class="mb-4"><img src="' + ssdThumbnail + '" alt="Thumbnail" class="' + thumbnailSize + '"></li>';
        prixTotal += prixSSD;
      }

      selectedOption = disqueDurSelect.selectedIndex;
      if (selectedOption !== 0) {
        const prixDisqueDur = parseFloat(disqueDurSelect.options[selectedOption].getAttribute('data-prix').replace(',', '.'));
        const disqueDurThumbnail = disqueDurSelect.options[selectedOption].getAttribute('data-thumbnail');
        composantsSelectionnes.innerHTML += '<li class="mb-4">' + disqueDurSelect.options[selectedOption].text + '</li>';
        composantsSelectionnes.innerHTML += '<li class="mb-4"><img src="' + disqueDurThumbnail + '" alt="Thumbnail" class="' + thumbnailSize + '"></li>';
        prixTotal += prixDisqueDur;
      }

      selectedOption = alimentationSelect.selectedIndex;
      if (selectedOption !== 0) {
        const prixAlimentation = parseFloat(alimentationSelect.options[selectedOption].getAttribute('data-prix').replace(',', '.'));
        const alimentationThumbnail = alimentationSelect.options[selectedOption].getAttribute('data-thumbnail');
        composantsSelectionnes.innerHTML += '<li class="mb-4">' + alimentationSelect.options[selectedOption].text + '</li>';
        composantsSelectionnes.innerHTML += '<li class="mb-4"><img src="' + alimentationThumbnail + '" alt="Thumbnail" class="' + thumbnailSize + '"></li>';
        prixTotal += prixAlimentation;
      }

      selectedOption = boitierSelect.selectedIndex;
      if (selectedOption !== 0) {
        const prixBoitier = parseFloat(boitierSelect.options[selectedOption].getAttribute('data-prix').replace(',', '.'));
        const boitierThumbnail = boitierSelect.options[selectedOption].getAttribute('data-thumbnail');
        composantsSelectionnes.innerHTML += '<li class="mb-4">' + boitierSelect.options[selectedOption].text + '</li>';
        composantsSelectionnes.innerHTML += '<li class="mb-4"><img src="' + boitierThumbnail + '" alt="Thumbnail" class="' + thumbnailSize + '"></li>';
        prixTotal += prixBoitier;
      }

      selectedOption = refroidissementSelect.selectedIndex;
      if (selectedOption !== 0) {
        const prixRefroidissement = parseFloat(refroidissementSelect.options[selectedOption].getAttribute('data-prix').replace(',', '.'));
        const refroidissementThumbnail = refroidissementSelect.options[selectedOption].getAttribute('data-thumbnail');
        composantsSelectionnes.innerHTML += '<li class="mb-4">' + refroidissementSelect.options[selectedOption].text + '</li>';
        composantsSelectionnes.innerHTML += '<li class="mb-4"><img src="' + refroidissementThumbnail + '" alt="Thumbnail" class="' + thumbnailSize + '"></li>';
        prixTotal += prixRefroidissement;
      }

      prixTotalElement.innerText = 'Prix total : ' + prixTotal.toFixed(2) + ' €';
      sauvegarderSelections();
    }

    document.addEventListener('DOMContentLoaded', chargerSelections);
    const selects = document.querySelectorAll('select');
    selects.forEach(select => select.addEventListener('change', updateRecapitulatif));



  </script>