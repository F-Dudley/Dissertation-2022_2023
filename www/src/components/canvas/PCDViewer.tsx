import { type ReactNode, forwardRef } from 'react';
import { LoaderProto, useLoader } from '@react-three/fiber';
import { Points } from '@react-three/drei';
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader.js';
import { BufferAttribute, type BufferGeometry } from 'three';

interface PCDViewerProps {
	dir: string;
	loader?: LoaderProto<undefined>;
	loading?: ReactNode;
	pointScale?: number;

	customColors?: Float32Array;
}

const PCDViewer = forwardRef<typeof Points | null, PCDViewerProps>(
	({ dir, loader, pointScale, customColors }, ref) => {
		const pcd: BufferGeometry = useLoader(loader ? loader : PLYLoader, dir);

		const { position, color } = pcd.attributes;

		return (
			<Points
				// eslint-disable-next-line @typescript-eslint/ban-ts-comment
				// @ts-ignore
				ref={ref}
				positions={(position as BufferAttribute).array as Float32Array}
				colors={
					customColors
						? customColors
						: pcd.hasAttribute('color')
						? ((color as BufferAttribute).array as Float32Array)
						: undefined
				}
				range={20}
			>
				<pointsMaterial
					size={pointScale ? pointScale : 0.0003}
					vertexColors
				/>
			</Points>
		);
	},
);

export default PCDViewer;
