
import React from "react";
import "../style/Body.css";

function Body() {
    return (
        <main className="body">

            <section className="announcement-box">

                {/* Image */}
                <section className="announcement-image">
                    <img
                        src="/images/expense-tracker.png"
                        alt="Expense tracker illustration"
                    />
                </section>

                {/* Text */}
                <section className="announcement-content">

                    <p className="announcement-subtitle">
                        Welcome
                    </p>

                    <h1 className="announcement-title">
                        Take Control of Your Expenses
                    </h1>

                    <p className="announcement-description">
                        Keep track of your spending, manage your budget,
                        and stay in control of your finances.
                    </p>

                    <button className="announcement-button">
                        Get Started
                    </button>

                </section>

            </section>

        </main>
    );
}

export default Body;

