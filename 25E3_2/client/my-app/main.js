import 'ol/ol.css';
import Map from 'ol/Map.js';
import View from 'ol/View.js';
import TileLayer from 'ol/layer/Tile.js';
import OSM from 'ol/source/OSM.js';
import { fromLonLat } from 'ol/proj.js';
import VectorLayer from 'ol/layer/Vector.js';
import VectorSource from 'ol/source/Vector.js';
import Feature from 'ol/Feature.js';
import Point from 'ol/geom/Point.js';
import { Style, Circle as CircleStyle, Fill, Stroke } from 'ol/style.js';

// =======================
// Vector source e layer
// =======================
const vectorSource = new VectorSource();
const vectorLayer = new VectorLayer({ source: vectorSource });

// =======================
// Carga inicial de pontos
// =======================
const starterPoints = await fetch('http://localhost:8000/getPoints');
const pointsData = await starterPoints.json();
const pointCollection = JSON.parse(pointsData);

pointCollection.features.forEach((point) => {
  const coords = fromLonLat(point.geometry.coordinates);
  const feature = new Feature({ geometry: new Point(coords) });

  feature.set('data', point.properties);

  if (point.properties.prediction) {
    feature.set('predictionResult', point.properties.prediction);
  }

  feature.setStyle(
    new Style({
      image: new CircleStyle({
        radius: 7,
        fill: new Fill({ color: 'red' }),
        stroke: new Stroke({ color: 'black', width: 2 }),
      }),
    })
  );

  vectorSource.addFeature(feature);
});

const map = new Map({
  target: 'map',
  layers: [
    new TileLayer({ source: new OSM() }),
    vectorLayer,
  ],
  view: new View({
    center: fromLonLat([-45.939373, -22.227077]),
    zoom: 13,
  }),
});

const modal = document.getElementById('point-modal');
const closeModalBtn = document.getElementById('close-modal');
const cancelarBtn = document.getElementById('cancelar');
const btnEnviar = document.getElementById('btnEnviar');

function openModal() { modal.classList.add('is-active'); }
function closeModal() { modal.classList.remove('is-active'); }


const infoModal = document.getElementById('info-modal');
const closeInfoModalBtn = document.getElementById('close-info-modal');
const infoContent = document.getElementById('info-content');

function openInfoModal() { infoModal.classList.add('is-active'); }
function closeInfoModal() { infoModal.classList.remove('is-active'); }

if (closeInfoModalBtn) {
  closeInfoModalBtn.addEventListener('click', closeInfoModal);
}

function showFeatureInfo(data) {
  infoContent.innerHTML = '';
  if (!data || Object.keys(data).length === 0) {
    infoContent.textContent = 'Nenhuma informação disponível.';
    return;
  }
  Object.entries(data).forEach(([key, value]) => {
    const p = document.createElement('p');
    p.innerHTML = `<strong>${key}:</strong> ${value}`;
    infoContent.appendChild(p);
  });
  openInfoModal();
}

let addPointMode = false;
let currentFeature = null;

const addPointBtn = document.getElementById('addPointBtn');
const clearPointsBtn = document.getElementById('clearPointsBtn');

addPointBtn.addEventListener('click', () => {
  addPointMode = !addPointMode;
  addPointBtn.classList.toggle('is-primary', addPointMode);
  addPointBtn.classList.toggle('is-link', !addPointMode);
});

clearPointsBtn.addEventListener('click', () => {
  vectorSource.clear();
});

cancelarBtn.addEventListener('click', () => {
  if (currentFeature) {
    vectorSource.removeFeature(currentFeature);
    currentFeature = null;
  }
  closeModal();
});

closeModalBtn.addEventListener('click', () => {
  if (currentFeature) {
    vectorSource.removeFeature(currentFeature);
    currentFeature = null;
  }
  closeModal();
});

map.on('singleclick', async (event) => {
  const coords = event.coordinate;

  const featureClicked = map.forEachFeatureAtPixel(event.pixel, (feature) => feature);
  if (featureClicked) {
    const data = featureClicked.get('data') || featureClicked.get('predictionResult');
    showFeatureInfo(data);
    return;
  }

  if (!addPointMode) {
    return;
  }

  const feature = new Feature({ geometry: new Point(coords) });
  feature.setStyle(
    new Style({
      image: new CircleStyle({
        radius: 7,
        fill: new Fill({ color: 'yellow' }),
        stroke: new Stroke({ color: 'black', width: 2 }),
      }),
    })
  );

  vectorSource.addFeature(feature);
  currentFeature = feature;
  openModal();

  // Envio de dados para previsão
  btnEnviar.onclick = async () => {
    const area_terreno = document.getElementById('area_terreno').value;
    const area_construida = document.getElementById('area_construida').value;
    const oferta = document.getElementById('oferta').value;
    const zonaHomogenea = document.getElementById('zonaHomogenea').value;
    const pavimentado = document.getElementById('pavimentado').checked ? 1 : 0;
    const corredorComercial = document.getElementById('corredorComercial').checked ? 1 : 0;
    const dataType = document.getElementById('itbiOferta').value === 'ITBI' ? 0 : 1;
    const typeStreet = document.getElementById('tipoVia').value;

    const payload = {
      terrain_area: area_terreno,
      built_area: area_construida,
      offer: oferta,
      zh: zonaHomogenea,
      is_paved: pavimentado,
      is_commercial: corredorComercial,
      data_type: dataType,
      street_type: typeStreet,
    };

    const result = await fetch('http://localhost:8000/newPrediction', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    const data = await result.json();

    feature.set('predictionResult', `${data} m²`);

    feature.setStyle(
      new Style({
        image: new CircleStyle({
          radius: 7,
          fill: new Fill({ color: 'blue' }),
          stroke: new Stroke({ color: 'white', width: 2 }),
        }),
      })
    );

    closeModal();
    currentFeature = null;
    addPointMode = false;
    addPointBtn.classList.remove('is-primary');
    addPointBtn.classList.add('is-link');
  };
});
