import { app } from '../../../scripts/app.js';
import { displayContext } from './common.js';

app.registerExtension({
  name: 'Crystools.Image.ShowResolution',
  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    if (nodeData.name === 'Image show resolution [Crystools]') {
      displayContext(nodeType, app, 0);
    }
  },
});

app.registerExtension({
  name: 'Crystools.Image.PreviewImageAdvance',
  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    if (nodeData.name === 'Preview image advance [Crystools]') {
      displayContext(nodeType, app, 0, true);
    }
  },
});