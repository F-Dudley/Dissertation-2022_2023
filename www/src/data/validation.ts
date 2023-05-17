import { SCANNING_TECHNIQUES, SCANNING_OBJECTS } from './constants';

export const IsAScanntingTechnique = (value: string): boolean => {
	return SCANNING_TECHNIQUES.includes(value);
};

export const IsAScanningObject = (value: string): boolean => {
	return SCANNING_OBJECTS.includes(value);
};
