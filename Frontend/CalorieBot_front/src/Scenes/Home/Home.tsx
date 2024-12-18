import Calculator from "../../Components/Calculator/Calculator";
import CalorieBurn from "../../Components/ChartCard/CalorieBurn/CalorieBurn";
import PieChartCard from "../../Components/ChartCard/PieChartCard/PieChartCard";
import SurfaceChart from "../../Components/ChartCard/SurfaceChart/SurfaceChart";
import "./Home.css";
function Home() {
  return (
    <>
      <div className="wrapper">
        <div className="container">
          <div className="calculator">
            <Calculator></Calculator>
          </div>
          <div className="stats">
            <CalorieBurn></CalorieBurn>
            <PieChartCard></PieChartCard>
            <SurfaceChart></SurfaceChart>
          </div>
          <div className="clear"></div>
        </div>
      </div>
    </>
  );
}

export default Home;
