import { type FC, type ReactNode, useMemo, forwardRef } from 'react';
import { LoaderProto, useLoader } from '@react-three/fiber';
import { Points } from '@react-three/drei';
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader.js';

interface PCDViewerProps {
	dir: string;
	loader?: LoaderProto<undefined>;
	loading?: ReactNode;
	pointScale?: number;
}

const PCDViewer: FC<PCDViewerProps> = forwardRef<typeof Points, PCDViewerProps>(
	({ dir, loader, pointScale }, ref) => {
		const pcd = useMemo(
			// eslint-disable-next-line react-hooks/rules-of-hooks
			() => useLoader(loader ? loader : PLYLoader, dir),
			[dir, loader],
		);

		return (
			<Points
				ref={ref}
				positions={pcd.attributes.position.array}
				colors={pcd.attributes.color.array}
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
