import React from "react";
import ReactDOM from "react-dom";
import renderer from "react-test-renderer";
import { mount } from "enzyme";

import IssueGroup from "./IssueGroup";
import Issue from "../issue/Issue";

const issueGroups = require("../../test_project_data/project_a.json");

describe("IssueGroup component", () => {
    test("Renders without crashing", () => {
        const div = document.createElement("div");
        ReactDOM.render(<IssueGroup />, div);
        ReactDOM.unmountComponentAtNode(div);
    });

    it("Renders correctly", () => {
        const tree = renderer.create(<IssueGroup />).toJSON();
        expect(tree).toMatchSnapshot();
    });

    describe("IssueGroup HTML elements", () => {
        it("should render a section element", () => {
            const wrapper = mount(<IssueGroup />);
            expect(wrapper.find("section").length).toEqual(1);
        });
        it("should render a h2 element", () => {
            const wrapper = mount(<IssueGroup />);
            expect(wrapper.find("h2").length).toEqual(1);
        });

        it("should render 2 i elements", () => {
            const wrapper = mount(<IssueGroup />);
            expect(wrapper.find("i").length).toEqual(2);
        });

        it("should render 3 div elements", () => {
            const wrapper = mount(<IssueGroup />);
            expect(wrapper.find("div").length).toEqual(3);
        });

        it("should render 2 Issue components", () => {
            const wrapper = mount(
                <IssueGroup issues={issueGroups["groups"][0].issues} />
            );
            expect(wrapper.find(Issue).length).toEqual(2);
        });
    });
});