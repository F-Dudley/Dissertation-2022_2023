import { Suspense, useMemo, useRef, useState } from 'react';
import { MathUtils, SphereGeometry, Vector3 } from 'three';
import { Points } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';

const MethodsPage = () => {
	const [registerClouds, setRegisterClouds] = useState<boolean>(false);
	const [showDistanceLines, setShowDistanceLines] = useState<boolean>(false);

	const smallSphereRef = useRef(null);
	const sphereRef = useRef(null);

	const smallerSphereGeometry = useMemo(
		() => new SphereGeometry(0.5, 32, 32),
		[],
	);
	const sphereGeometry = useMemo(() => new SphereGeometry(1, 32, 32), []);

	const calcLinePoints = useMemo(() => {
		const smallPoints = smallerSphereGeometry.attributes.position;
		const bigPoints = sphereGeometry.attributes.position;

		const points = new Float32Array(bigPoints.count * 6);

		for (let i = 0; i < bigPoints.count; i++) {
			points[i * 6] = smallPoints.array[i];
			points[i * 6 + 1] = smallPoints.array[i + 1];
			points[i * 6 + 2] = smallPoints.array[i + 2];
			points[i * 6 + 3] = bigPoints.array[i];
			points[i * 6 + 4] = bigPoints.array[i + 1];
			points[i * 6 + 5] = bigPoints.array[i + 2];
		}

		return points;
	}, [smallerSphereGeometry, sphereGeometry]);

	useFrame((_, delta) => {
		if (smallSphereRef.current !== null) {
			smallSphereRef.current.position.lerp(
				registerClouds ? new Vector3(0, 0, 0) : new Vector3(2, 0, 0),
				0.1,
			);
		}
		if (sphereRef.current !== null) {
			sphereRef.current.position.lerp(
				registerClouds ? new Vector3(0, 0, 0) : new Vector3(-2, 0, 0),
				0.1,
			);
		}
	});

	return (
		<>
			<Suspense fallback={null}>
				<mesh ref={smallSphereRef} position={[2, 0, 0]}>
					<Points
						positions={
							smallerSphereGeometry.attributes.position.array
						}
					>
						<pointsMaterial size={0.01} color="green" />
					</Points>
				</mesh>
				<mesh ref={sphereRef} position={[-2, 0, 0]}>
					<Points
						positions={sphereGeometry.attributes.position.array}
					>
						<pointsMaterial size={0.01} color="red" />
					</Points>
				</mesh>
				{showDistanceLines && (
					<mesh>
						<lineSegments>
							<shapeGeometry attach="geometry" />
							<bufferGeometry>
								<bufferAttribute
									attach={'attributes-position'}
									count={calcLinePoints.length / 3}
									array={calcLinePoints}
									itemSize={3}
								/>
							</bufferGeometry>
							<lineBasicMaterial color="yellow" />
						</lineSegments>
					</mesh>
				)}
			</Suspense>
		</>
	);
};

export default MethodsPage;
