import { SphereGeometry, type BufferAttribute } from 'three';

export const DemoSpherePoints = (
	width: number,
	widthSegments: number,
	heightSegments: number,
): BufferAttribute => {
	const sphereGeo = new SphereGeometry(width, widthSegments, heightSegments);

	const spherePosAttr = sphereGeo.getAttribute('position') as BufferAttribute;

	return spherePosAttr;
};

export const DemoSphereLines = (
	spherePosAttr1: BufferAttribute,
	spherePosAttr2: BufferAttribute,
): Float32Array => {
	if (
		!spherePosAttr1 ||
		!spherePosAttr2 ||
		spherePosAttr1.count !== spherePosAttr2.count
	) {
		throw new Error('Invalid or Incompatible geometries');
	}

	const arrLen = (spherePosAttr1.count + spherePosAttr2.count) * 3;
	const returnArr = new Float32Array(arrLen);

	for (let index = 0; index < spherePosAttr1.count; index++) {
		const arrIndex = index * 6;

		returnArr[arrIndex] = spherePosAttr1.getX(index);
		returnArr[arrIndex + 1] = spherePosAttr1.getY(index);
		returnArr[arrIndex + 2] = spherePosAttr1.getZ(index);
		returnArr[arrIndex + 3] = spherePosAttr2.getX(index);
		returnArr[arrIndex + 4] = spherePosAttr2.getY(index);
		returnArr[arrIndex + 5] = spherePosAttr2.getZ(index);
	}

	return returnArr;
};
