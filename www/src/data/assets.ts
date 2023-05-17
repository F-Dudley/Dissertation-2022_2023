// Dist Colour Maps

import { SCANNING_TECHNIQUES } from './constants';

export const getDistMapURL = (techniqueID: string) => {
	if (!SCANNING_TECHNIQUES.includes(techniqueID))
		throw new Error(`Invalid techniqueID: ${techniqueID}`);

	return new URL(`./dist-maps/${techniqueID}.json`, import.meta.url).href;
};

export const DistMaps = new Map();

import { vertex as KinectVertex } from './dist-maps/Kinect.json';
import { vertex as PolyCamVertex } from './dist-maps/PolyCam.json';
import { vertex as Point_EVertex } from './dist-maps/Point_E.json';

DistMaps.set('Kinect', KinectVertex.flat(2));
DistMaps.set('PolyCam', PolyCamVertex.flat(2));
DistMaps.set('Point_E', Point_EVertex.flat(2));
