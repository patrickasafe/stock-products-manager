import type { NextPage } from "next";
import EnchancedTable from "../../components/EnchancedTable";
import styles from "../../styles/Home.module.css";

import { useProducts } from "../../components/EnchancedTable/hooks/useProducts";
import { productsTableHeadCells as headCells } from "../../components/EnchancedTable/utils/configs";

const Products: NextPage = () => {
  const [products, setProducts] = useProducts();

  return (
    <div className={styles.container}>
      <EnchancedTable headCells={headCells} data={products} setData={setProducts} />
    </div>
  );
};
export default Products;
