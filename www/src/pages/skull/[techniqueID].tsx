import { useParams } from 'react-router-dom';

import View from '@/components/canvas/View';
import PCDViewer from '@/components/canvas/PCDViewer';
import { SCANNING_TECHNIQUES } from '@/data/constants';
import Root from '@/components/tunnels/Root';

const SkullTechniqueID = () => {
	const { techniqueID } = useParams();

	if (!SCANNING_TECHNIQUES.includes(techniqueID as string) || !techniqueID) {
		console.log(`TechniqueID: ${techniqueID} is not a valid technique ID.`);
		return (
			<Root.In>
				<h1>404</h1>
			</Root.In>
		);
	}

	const cloudDir = `/clouds/${techniqueID}/skull.ply`;

	return (
		<View>
			<PCDViewer
				dir={cloudDir}
				loading={
					<div>
						<h1>LOADING</h1>
					</div>
				}
			/>
		</View>
	);
};

export default SkullTechniqueID;
