import { Suspense, useMemo, useRef, useState } from 'react';
import { type BufferAttribute, Vector3, Mesh } from 'three';
import { Points } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';
import { DemoSphereLines, DemoSpherePoints } from '@/utils/three';

const MethodsPage = () => {
	const [registerClouds, setRegisterClouds] = useState<boolean>(true);
	const [showDistanceLines, setShowDistanceLines] = useState<boolean>(true);

	const smallSphereRef = useRef<Mesh>(null);
	const sphereRef = useRef<Mesh>(null);

	const smallSpherePos = useMemo<BufferAttribute>(
		() => DemoSpherePoints(0.5, 15, 15),
		[],
	);
	const largeSpherePos = useMemo<BufferAttribute>(
		() => DemoSpherePoints(1, 15, 15),
		[],
	);

	const LinePoints = useMemo(() => {
		return DemoSphereLines(smallSpherePos, largeSpherePos);
	}, [smallSpherePos, largeSpherePos]);

	useFrame(() => {
		if (smallSphereRef.current !== null) {
			smallSphereRef.current.position.lerp(
				registerClouds ? new Vector3(0, 0, 0) : new Vector3(2, 0, 0),
				0.1,
			);
		}
		if (sphereRef.current !== null) {
			sphereRef.current.position.lerp(
				registerClouds ? new Vector3(0, 0, 0) : new Vector3(-2.5, 0, 0),
				0.1,
			);
		}
	});

	return (
		<>
			<Suspense fallback={null}>
				<mesh ref={smallSphereRef} position={[2, 0, 0]}>
					<Points positions={smallSpherePos.array as Float32Array}>
						<pointsMaterial size={0.01} color="green" />
					</Points>
				</mesh>
				<mesh ref={sphereRef} position={[-2, 0, 0]}>
					<Points positions={largeSpherePos.array as Float32Array}>
						<pointsMaterial size={0.01} color="red" />
					</Points>
				</mesh>
				{showDistanceLines && (
					<mesh>
						<lineSegments>
							<bufferGeometry>
								<bufferAttribute
									attach={'attributes-position'}
									args={[LinePoints, 3]}
								/>
							</bufferGeometry>
							<lineBasicMaterial color="blue" opacity={0.05} />
						</lineSegments>
					</mesh>
				)}
			</Suspense>
		</>
	);
};

export default MethodsPage;
